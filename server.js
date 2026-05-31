const http = require('http');
const fs = require('fs');
const path = require('path');

const PORT = 8080;
const PUBLIC_DIR = __dirname;

const mimeTypes = {
  '.html': 'text/html',
  '.css': 'text/css',
  '.js': 'application/javascript',
  '.json': 'application/json',
  '.png': 'image/png',
  '.jpg': 'image/jpeg',
  '.jpeg': 'image/jpeg',
  '.gif': 'image/gif',
  '.svg': 'image/svg+xml',
  '.ico': 'image/x-icon',
  '.woff': 'font/woff',
  '.woff2': 'font/woff2',
  '.ttf': 'font/ttf',
  '.eot': 'application/vnd.ms-fontobject',
  '.otf': 'font/otf',
  '.txt': 'text/plain',
  '.1': 'text/html'
};

const server = http.createServer((req, res) => {
  // Log request
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.url}`);

  // Decode URL to handle spaces and special characters
  let decodedUrl = decodeURIComponent(req.url);
  
  // Remove query parameters
  let cleanUrl = decodedUrl.split('?')[0];
  
  // Resolve path
  let filePath = path.join(PUBLIC_DIR, cleanUrl);
  
  // If it's a directory, try serving index.html inside it
  fs.stat(filePath, (err, stats) => {
    if (!err && stats.isDirectory()) {
      filePath = path.join(filePath, 'index.html');
    }
    
    // Check if file exists
    fs.access(filePath, fs.constants.F_OK, (err) => {
      if (err) {
        // If file doesn't exist, check if we can serve it as a root page directly (e.g. /about -> about.1 or /about -> about/index.html)
        // If the URL has no extension, try appending .1 or looking for it
        if (!path.extname(filePath)) {
          let altPath1 = filePath + '.1';
          let altPath2 = path.join(filePath, 'index.html');
          
          fs.access(altPath1, fs.constants.F_OK, (err1) => {
            if (!err1) {
              serveFile(altPath1, res);
            } else {
              fs.access(altPath2, fs.constants.F_OK, (err2) => {
                if (!err2) {
                  serveFile(altPath2, res);
                } else {
                  console.log(`  -> 404 Not Found (Directory/Alt files checked)`);
                  serve404(res);
                }
              });
            }
          });
        } else {
          console.log(`  -> 404 Not Found: ${filePath}`);
          serve404(res);
        }
      } else {
        serveFile(filePath, res);
      }
    });
  });
});

function serveFile(filePath, res) {
  // Determine content type by looking at filename before '@' or '?'
  let baseFilename = path.basename(filePath).split('@')[0].split('?')[0];
  let ext = path.extname(baseFilename).toLowerCase();
  
  let contentType = mimeTypes[ext] || 'application/octet-stream';
  
  // Handle files like 'nostalgia-workshop' which have no extension
  if (baseFilename === 'nostalgia-workshop' || ext === '.1') {
    contentType = 'text/html';
  }
  
  fs.readFile(filePath, (err, content) => {
    if (err) {
      console.log(`  -> 500 Server Error reading: ${filePath}`);
      res.writeHead(500);
      res.end(`Server Error: ${err.code}`);
    } else {
      console.log(`  -> 200 OK (${contentType}) - size: ${content.length} bytes`);
      res.writeHead(200, { 'Content-Type': contentType });
      res.end(content, 'utf-8');
    }
  });
}

function serve404(res) {
  res.writeHead(404, { 'Content-Type': 'text/html' });
  res.end('<h1>404 Not Found</h1><p>The requested URL was not found on this server.</p>');
}

server.listen(PORT, () => {
  console.log(`Custom server running at http://localhost:${PORT}/`);
  console.log(`Serving static files from ${PUBLIC_DIR}`);
});
