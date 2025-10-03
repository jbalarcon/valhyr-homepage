#!/usr/bin/env python3
import re

# Read the HTML file
with open('/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned.html', 'r') as f:
    html_content = f.read()

# New header HTML to insert
new_header_html = '''
        
        <!-- NEW REDESIGNED HEADER LAYOUT -->
        <div class="header_content-redesigned">
            
            <!-- Hero Headings -->
            <div class="hero-headings" animate="h1">
                <h2 class="hero-heading heading-style-h0">Sourcer l'exception.</h2>
                <h2 class="hero-heading heading-style-h0">Ouvrir les possibles.</h2>
            </div>
            
            <!-- Tagline -->
            <h1 class="hero-tagline heading-style-h3" animate="header-item">
                L'acteur de référence de l'evergreen en France
            </h1>
            
            <!-- Description -->
            <p class="hero-description" animate="header-item">
                Fondé sur une approche quantitative innovante, Valhyr Capital développe des produits financiers inédits à la croisée des marchés privés, marchés publics et des actifs alternatifs.
            </p>
            
            <!-- CTA Button -->
            <div class="hero-ctas" animate="header-item">
                <a data-wf--button--variant="base" href="/contact" class="button w-inline-block">
                    <div class="button_wrap">
                        <div class="button_clip">
                            <div class="button_content">
                                <div class="button_text">Nous contacter</div>
                                <div class="button_icon">
                                    <img src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683d982e34f4992ea3bc67e5_arrow-up-right.svg" loading="lazy" alt="" class="g_svg"/>
                                </div>
                            </div>
                            <div class="button_content is-asbolute">
                                <div class="button_text">Nous contacter</div>
                                <div class="button_icon">
                                    <img src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683d982e34f4992ea3bc67e5_arrow-up-right.svg" loading="lazy" alt="" class="g_svg"/>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div class="button-text_line"></div>
                </a>
            </div>
            
            <!-- Logo Section -->
            <div class="logo_header-redesigned">
                <div class="logo-title">Ils nous font confiance</div>
                
                <!-- Desktop Logo Grid -->
                <div class="logo-grid">
                    <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683834638dbc9a87bdedd724_neuber.svg" alt="Neuberger Berman"/>
                    <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683834630a6fcad585f4467c_morgan.svg" alt="Morgan Stanley"/>
                    <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/6838346380332e170e6adefc_eqt.svg" alt="EQT"/>
                    <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/6838346386aee080076f36b2_goldman-sachs-2-1%201.svg" alt="Goldman Sachs"/>
                    <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683834634c53927935e70c19_Subtract.svg" alt="Blackstone"/>
                </div>
                
                <!-- Mobile Logo Slider -->
                <div class="splide is-logos logo-slider">
                    <div class="splide__track is-logos">
                        <div class="splide__list is-logos">
                            <div class="splide__slide is-logos">
                                <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683834638dbc9a87bdedd724_neuber.svg" alt="" class="logo1_logo"/>
                            </div>
                            <div class="splide__slide is-logos">
                                <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683834630a6fcad585f4467c_morgan.svg" alt="" class="logo1_logo"/>
                            </div>
                            <div class="splide__slide is-logos">
                                <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/6838346380332e170e6adefc_eqt.svg" alt="" class="logo1_logo"/>
                            </div>
                            <div class="splide__slide is-logos">
                                <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/6838346386aee080076f36b2_goldman-sachs-2-1%201.svg" alt="" class="logo1_logo"/>
                            </div>
                            <div class="splide__slide is-logos">
                                <img loading="lazy" src="https://cdn.prod.website-files.com/68381555c2de698ae140b848/683834634c53927935e70c19_Subtract.svg" alt="" class="logo1_logo"/>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            
        </div>
        
'''

# Find the position after </div></div> that closes logo_header-home and header_content
# We want to insert right after container-large opens
marker = '<header class="section_header"><div class="padding-global"><div class="container-large">'
marker_pos = html_content.find(marker)

if marker_pos != -1:
    insert_pos = marker_pos + len(marker)
    html_content = html_content[:insert_pos] + new_header_html + html_content[insert_pos:]
    
    # Write back
    with open('/Users/jean-baptistealarcon/coding/valhyr/homepage-redesigned.html', 'w') as f:
        f.write(html_content)
    
    print("✓ New header HTML successfully inserted!")
else:
    print("✗ Marker not found")
