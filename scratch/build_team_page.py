import os
import re

about_file = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\about.1"
team_dir = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\team"
team_index = os.path.join(team_dir, "index.html")
team_dot_1 = r"c:\Users\samir\OneDrive\Desktop\confidential\ninaanddarek.com\team.1"

# Create team directory if it doesn't exist
os.makedirs(team_dir, exist_ok=True)

with open(about_file, 'r', encoding='utf-8', errors='ignore') as f:
    html = f.read()

# 1. Update metadata
html = html.replace(
    '<title>About - Sabhya Prajapati Wedding Photography Europe</title>',
    '<title>Team - Sabhya Prajapati Wedding Photography Europe</title>'
)
html = html.replace(
    '<meta name="description" content="Few words about us, and our philosophy. Sabhya Prajapati, wedding photographers based in Poland, but photographing love stories all over Europe" />',
    '<meta name="description" content="Meet our collective of visual storytellers, wedding photographers, videographers, and editors at Sabhya Prajapati Wedding Photography." />'
)
html = html.replace(
    '<link rel="canonical" href="about.1" />',
    '<link rel="canonical" href="team.1" />'
)
html = html.replace(
    '<meta property="og:title" content="About - Sabhya Prajapati Wedding Photography Europe" />',
    '<meta property="og:title" content="Team - Sabhya Prajapati Wedding Photography Europe" />'
)
html = html.replace(
    '<meta property="og:description" content="Few words about us, and our philosophy. Sabhya Prajapati, wedding photographers based in Poland, but photographing love stories all over Europe" />',
    '<meta property="og:description" content="Meet our collective of visual storytellers, wedding photographers, videographers, and editors at Sabhya Prajapati Wedding Photography." />'
)
html = html.replace(
    '<meta property="og:url" content="https://ninaanddarek.com/about/" />',
    '<meta property="og:url" content="https://ninaanddarek.com/team/" />'
)

# Yoast Schema Updates
html = html.replace('"url":"https://ninaanddarek.com/about/"', '"url":"https://ninaanddarek.com/team/"')
html = html.replace('"name":"About - Sabhya Prajapati Wedding Photography Europe"', '"name":"Team - Sabhya Prajapati Wedding Photography Europe"')
html = html.replace('{"@type":"ListItem","position":2,"name":"About"}', '{"@type":"ListItem","position":2,"name":"Team"}')

# 2. De-activate "ABOUT" menu items highlights
html = html.replace(
    'class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-83 current_page_item menu-item-96"',
    'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-96"'
)
html = html.replace(
    'aria-current="page" class="elementor-item elementor-item-active"',
    'class="elementor-item"'
)
# Update mobile menu item highlighted state if there are any
html = html.replace(
    'class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item page-item-83 current_page_item menu-item-96"',
    'class="menu-item menu-item-type-post_type menu-item-object-page menu-item-96"'
)

# 3. Add custom styles inside the head section (before </head>)
custom_css = """
	<style>
		/* Custom overrides for Team Page background */
		.elementor-83 .elementor-element.elementor-element-272226e:not(.elementor-motion-effects-element-type-background),
		.elementor-83 .elementor-element.elementor-element-272226e > .elementor-motion-effects-container > .elementor-motion-effects-layer {
			background-image: url("https://ik.imagekit.io/logicsync/tr:w-2000/photo%202.JPG") !important;
			background-position: center 60% !important;
		}

		/* Team Grid Styling */
		.team-grid-container {
			display: grid;
			grid-template-columns: repeat(3, 1fr);
			gap: 50px 30px;
			margin: 20px auto 0 auto;
			width: 100%;
			max-width: 1000px;
		}

		.team-card {
			display: flex;
			flex-direction: column;
			align-items: center;
			text-align: center;
			background-color: transparent;
		}

		.team-image-wrapper {
			position: relative;
			width: 100%;
			aspect-ratio: 3/4;
			overflow: hidden;
			margin-bottom: 20px;
			border: 1px solid rgba(255, 255, 255, 0.15);
			background-color: #0b0b0b;
		}

		/* Hover overlay slide/fade for bio text */
		.team-hover-overlay {
			position: absolute;
			top: 0;
			left: 0;
			width: 100%;
			height: 100%;
			background: rgba(0, 0, 0, 0.82);
			display: flex;
			align-items: center;
			justify-content: center;
			padding: 25px;
			opacity: 0;
			transition: opacity 0.4s ease;
			box-sizing: border-box;
		}

		.team-card:hover .team-hover-overlay {
			opacity: 1;
		}

		.team-bio {
			color: #e0e0e0;
			font-family: 'Merriweather', Serif;
			font-size: 13.5px;
			line-height: 1.6;
			margin: 0;
		}

		.team-name {
			font-family: 'Cormorant Garamond', Sans-serif;
			font-size: 24px;
			font-weight: 300;
			color: #ffffff;
			margin: 0 0 5px 0;
			letter-spacing: 0.5px;
			text-transform: uppercase;
		}

		.team-role {
			font-family: 'Montserrat', Sans-serif;
			font-size: 11px;
			font-weight: 400;
			color: #bababa;
			text-transform: uppercase;
			letter-spacing: 1px;
			margin: 0;
		}

		/* Responsive Breakpoints */
		@media (max-width: 959px) {
			.team-grid-container {
				grid-template-columns: repeat(2, 1fr);
				gap: 40px 20px;
			}
			.team-name {
				font-size: 22px;
			}
		}

		@media (max-width: 600px) {
			.team-grid-container {
				grid-template-columns: 1fr;
				gap: 30px;
				max-width: 400px;
				margin: 20px auto 0 auto;
			}
		}
	</style>
</head>
"""

html = html.replace('</head>', custom_css)

# 4. Define our new page content
new_content_body = """
				<section class="elementor-section elementor-top-section elementor-element elementor-element-272226e elementor-section-stretched elementor-section-full_width elementor-section-height-min-height elementor-section-items-top elementor-section-content-top elementor-section-height-default" data-id="272226e" data-element_type="section" data-e-type="section" data-settings="{&quot;stretch_section&quot;:&quot;section-stretched&quot;,&quot;background_background&quot;:&quot;classic&quot;}">
						<div class="elementor-container elementor-column-gap-no">
					<div class="elementor-column elementor-col-100 elementor-top-column elementor-element elementor-element-faae073" data-id="faae073" data-element_type="column" data-e-type="column">
			<div class="elementor-widget-wrap">
							</div>
		</div>
					</div>
		</section>
		
		<section class="elementor-section elementor-top-section elementor-element elementor-section-boxed elementor-section-height-default elementor-section-height-default">
			<div class="elementor-container elementor-column-gap-wider">
				<div class="elementor-column elementor-col-100 elementor-top-column elementor-element">
					<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-widget elementor-widget-heading" style="text-align: center; margin-top: 80px; margin-bottom: 20px;">
							<div class="elementor-widget-container">
								<h1 class="elementor-heading-title elementor-size-xl" style="font-family: 'Cormorant Garamond', Sans-serif; font-size: 55px; font-weight: 300; text-transform: uppercase; letter-spacing: 2px;">Meet The Team</h1>
							</div>
						</div>
						<div class="elementor-element elementor-widget elementor-widget-text-editor" style="text-align: center; max-width: 800px; margin: 0 auto 10px auto;">
							<div class="elementor-widget-container">
								<p style="font-family: 'Merriweather', Serif; font-size: 16px; line-height: 1.8; color: #bababa; font-style: italic;">
									We are a collective of visual storytellers, artists, and creators. We don’t just capture weddings—we document love in its rawest, most emotional, and cinematic form. Inspired by natural light, timeless art, and real connection, each of us brings a unique perspective to preserving your stories.
								</p>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section class="elementor-section elementor-top-section elementor-element elementor-section-boxed elementor-section-height-default elementor-section-height-default">
			<div class="elementor-container elementor-column-gap-wider">
				<div class="elementor-column elementor-col-100 elementor-top-column elementor-element">
					<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-widget elementor-widget-image" style="text-align: center; margin-top: -45px; margin-bottom: 50px;">
							<div class="elementor-widget-container">
								<img decoding="async" src="https://ik.imagekit.io/logicsync/iageyyhrjr.png" alt="Collective Showcase" style="max-width: 400px; width: 100%; height: auto; display: block; margin: 0 auto;" />
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>

		<section class="elementor-section elementor-top-section elementor-element elementor-section-boxed elementor-section-height-default elementor-section-height-default" style="padding-bottom: 80px;">
			<div class="elementor-container elementor-column-gap-wider">
				<div class="elementor-column elementor-col-100 elementor-top-column elementor-element">
					<div class="elementor-widget-wrap elementor-element-populated">
						
						<div class="team-grid-container">
							<!-- Member 1 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Founder of the collective. Deeply inspired by classic cinema, natural light, and the quiet beauty of rural spaces.</p>
									</div>
								</div>
								<h3 class="team-name">Sabhya Prajapati</h3>
								<p class="team-role">Founder & Lead Photographer</p>
							</div>

							<!-- Member 2 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Co-creative mind behind the aesthetic direction, obsessed with rich color grading and moody editorial layouts.</p>
									</div>
								</div>
								<h3 class="team-name">Elena Rostova</h3>
								<p class="team-role">Co-Creative Director & Editor</p>
							</div>

							<!-- Member 3 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Specialist in capturing moving frames. Believes that every glance and whisper has a rhythm that belongs on film.</p>
									</div>
								</div>
								<h3 class="team-name">Darek Kowalski</h3>
								<p class="team-role">Lead Cinematographer</p>
							</div>

							<!-- Member 4 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Brings editorial concepts to life. Combines styling with visual architecture to create effortless, elegant scenes.</p>
									</div>
								</div>
								<h3 class="team-name">Nina Nowak</h3>
								<p class="team-role">Art Director & Stylist</p>
							</div>

							<!-- Member 5 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Senior photographer specializing in industrial and alternative venues. Focuses on shadows, grit, and emotional depth.</p>
									</div>
								</div>
								<h3 class="team-name">Marcus Thorne</h3>
								<p class="team-role">Senior Photographer</p>
							</div>

							<!-- Member 6 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Capturing elopements in the most remote corners of the world. Driven by untamed nature and wild, unscripted love stories.</p>
									</div>
								</div>
								<h3 class="team-name">Aria Bennett</h3>
								<p class="team-role">Associate Photographer</p>
							</div>

							<!-- Member 7 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">An expert in low-light and flash techniques. Blends classic painting compositions with modern editorial wedding portraiture.</p>
									</div>
								</div>
								<h3 class="team-name">Julian Vance</h3>
								<p class="team-role">Lighting Specialist</p>
							</div>

							<!-- Member 8 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Connecting the dots across borders. Ensures that our international elopements and destination shoots run seamlessly.</p>
									</div>
								</div>
								<h3 class="team-name">Clara Dubois</h3>
								<p class="team-role">Destination Coordinator</p>
							</div>

							<!-- Member 9 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Always finding the unexpected angle. Combines aerial drone layouts with dynamic candid moments from the ground.</p>
									</div>
								</div>
								<h3 class="team-name">Lucas Moreau</h3>
								<p class="team-role">Drone Operator & Second</p>
							</div>

							<!-- Member 10 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Crafts the final visual language of every collection. Master of fine art black and whites and warm, nostalgic tones.</p>
									</div>
								</div>
								<h3 class="team-name">Sophia Lindqvist</h3>
								<p class="team-role">Head of Post-Production</p>
							</div>

							<!-- Member 11 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">Combines Super 8 vintage textures with high-definition digital cinema, focusing on custom audio design for wedding films.</p>
									</div>
								</div>
								<h3 class="team-name">Ethan Brooks</h3>
								<p class="team-role">Film Videographer</p>
							</div>

							<!-- Member 12 -->
							<div class="team-card">
								<div class="team-image-wrapper">
									<div class="team-hover-overlay">
										<p class="team-bio">The first voice you hear and the heart of our operations. Manages booking details, consulting, and client experience.</p>
									</div>
								</div>
								<h3 class="team-name">Maya Patil</h3>
								<p class="team-role">Studio Manager</p>
							</div>
						</div>

					</div>
				</div>
			</div>
		</section>

		<section class="elementor-section elementor-top-section elementor-element elementor-section-boxed elementor-section-height-default elementor-section-height-default" style="padding-bottom: 100px;">
			<div class="elementor-container elementor-column-gap-default">
				<div class="elementor-column elementor-col-100 elementor-top-column elementor-element">
					<div class="elementor-widget-wrap elementor-element-populated">
						<div class="elementor-element elementor-widget elementor-widget-text-editor" style="text-align: center; margin-bottom: 20px;">
							<div class="elementor-widget-container">
								<p style="font-family: 'Merriweather', Serif; font-size: 15px; color: #bababa; font-style: italic;">
									Ready to document your story with us?
								</p>
							</div>
						</div>
						<div class="elementor-element elementor-align-center elementor-widget elementor-widget-button">
							<div class="elementor-widget-container">
								<div class="elementor-button-wrapper" style="text-align: center;">
									<a class="elementor-button elementor-button-link elementor-size-lg" href="contact.1">
										<span class="elementor-button-content-wrapper">
											<span class="elementor-button-text">GET IN TOUCH!</span>
										</span>
									</a>
								</div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</section>
"""

# Replace content of the elementor-83 container (between container div and footer)
# Regex to find: <div data-elementor-type="wp-page" data-elementor-id="83" class="elementor elementor-83" data-elementor-post-type="page"> ... <footer data-elementor-type="footer"
pattern = re.compile(
    r'(<div data-elementor-type="wp-page" data-elementor-id="83" class="elementor elementor-83" data-elementor-post-type="page">).*?(<footer data-elementor-type="footer")',
    re.DOTALL
)

new_html, count = pattern.subn(rf'\1\n{new_content_body}\n\t\t\t\t</div>\n\t\t\t\t\2', html)

if count > 0:
    print("Successfully replaced body content inside elementor-83 container.")
    
    # Save to team/index.html
    with open(team_index, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Saved team page to {team_index}")
    
    # Save to team.1
    with open(team_dot_1, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Saved team page to {team_dot_1}")
else:
    print("ERROR: Did not find the elementor-83 container block to replace.")
