function TopicsPage() {
      return (
          <>
            <h2>WEB DEV CONCEPTS</h2>
            <nav class="local">
                <a href="#webServers">Web Servers</a>
                <a href="#frontendDesign">Frontend Design</a>
                <a href="#optimizingImages">Optimizing Images</a>
                <a href="#favicons">Favicons</a>
            </nav>
            <article id="webServers">
                <h3>WEB SERVERS</h3>
                    <p>
                        A <strong>designated homepage</strong> usually refers to a website's or a web server's "index.html" file. 
                        This file is retrieved by the web application when the <strong>URL</strong> input by the user
                        specifies the <strong>path</strong> to the root directory. The GET request is placed, and the web application
                        retrieves the "index.html" file as a default access point for the user. In the case of the .NET platform from
                        Microsoft, the designated homepage is titled "defaul.html". In other examples, the index file is not an HTML file
                        but a JSON or PHP file, depending on the server.
                    </p>
                    <p>
                        The General section of the Headers tab in the Inspector's Network screen displays the URL, the <strong>request method</strong>,
                        <strong>IP address</strong> and referrer policy. The "Response Headers" section displays content length and type, date accessed,
                        date modified, among other information. The longest section is that of the Request Headers, which specifies the cookie data as well
                        as the browser and platform information.
                        In comparison, accessing the file from the local computer instead of the web server displays some differences in the information displayed in the 
                        Inspector Network tab. The request method, status code, and referrer method remain the same, but the URL is entirely different save for the 
                        index.html resource at the end. The URL from the web server displays the HTTPS <strong>scheme</strong>, while the URL from the local computer
                        displays the File scheme. Further, the Response Headers section in the latter case only contains the content type and the date last modified. 
                        The Request Headers section is equally sparse, containing only the browser information as well as the computer platform.
                    </p>
                    <p>
                        The <strong>favicon</strong> file has a status code of 200 which means that the request was successful. In this particular case, the GET request was placed.
                        This process was successful because the OSU server provided the favicon automatically and thus, the GET request was able to find it and utilize it in its response.
                        In contrast, the "main.css" and "main.js" files had status codes of 404 which means that the resource was not found, and thus the GET request was unsuccessful.
                        This is due to the fact that both these files have not been created yet, even though they are referenced in the <strong>boilerplate</strong>.
                    </p>
                    <p>
                        The <strong>scheme</strong> of a URL is followed by a colon and refers to the protocol used by the web client to send a request. In my URL, the scheme is HTTPS, which adds encryption to the data
                        being exchanged. Additional schemes include HTTP, FTP, FTPS, SMS, and File which denote different processes and/or encryption. 
                        The <strong>host domain</strong> name of a URL is preceded by two slashes and specifies the machine to which the request must be sent. In this case, the host domain is "oregonstate.edu".
                        The DNS server receives the request with the domain name and returns the IP address to which the domain name is mapped. The browser will then use the IP address to navigate to its destination.
                        The <strong>subdomain</strong> name precedes the host domain name in the URL and is a subdivision of the primary domain. The subdivision for my URL is "web" and "engr". 
                        Finally, The <strong>resources</strong> in a URL are denoted after a slash, which indicate the file path to that resource. These resources may be <strong>static</strong>, such as in my URL,
                        which incorporates a text file found at "~__/_folder_/index.html". Resources may also be <strong>dynamically generated</strong>, which executes a program when that file path is accessed.
                    </p>
            </article>
            <article id="frontendDesign">
                <h3>FRONTEND DESIGN</h3>
                    <p>
                        <strong>Frontend Design</strong> refers to the aspect of web development that involves the construction of what the user sees when they're visiting and interacting with a site.
                        The successful selection and implementation of appropriate fonts, colors, media elements, and methods of navigation positively influences the user's overall experience on a website.
                        For this reason, a good frontend designer will take into account how accessible the features of the webpage are and how efficiently the user can engage with it to accomplish a task. 
                        If a website's appearance and features are unintuitive, uninviting, or involve too many steps, the user's experience will suffer as a result.
                        For this reason, strong frontend design adequately tailors the visual aspects of a webpage and its interface to create an appealing and positive exterior with the means to fulfill
                        the user's demand as promptly and pleasantly as possible.
                        A webpage with strong frontend design results in high  <strong>usability</strong> and improves the likelihood that a user will make a repeat visit to that webpage.
                        Listed below are the <strong>Five "E"s</strong> of high website usability.
                    </p>
                    <dl>
                        <dt>Effective</dt>
                        <dd>The website is consistent, accurate, and is capable of enabling the user to successfully accomplish their task.</dd>
                        <dt>Efficient</dt>
                        <dd>The website is structured in a way that helps the user accomplish their task quickly and without unnecessary steps.</dd>
                        <dt>Easy to Navigate</dt>
                        <dd>The website is laid out in an intuitive manner that ensures the user can find what they need, both as a novice
                            and as a repeat user.
                        </dd>
                        <dt>Error-free</dt>
                        <dd>The website is logically sound and has no careless mistakes that could detract from the website's use.</dd>
                        <dt>Enjoyable</dt>
                        <dd>The website is visually appealing and interactively engaging for the user.
                        </dd>
                    </dl>
                    <p>
                        HTML utilizes <strong>page layout tags</strong> to specify the different portions of the content on the page.
                        The <strong>header</strong> element is the topmost part of a webpage and usually displays the website's name
                        and slogan. This element is often the same across the different pages of the website.
                        The <strong>main</strong> element holds the majority of the content on the webpage.
                        Additionally, the <strong>section</strong> element groups the content of the main element into its respective parts, 
                        typically with a headline to introduce it.
                        Moreover, the <strong>article</strong> element further groups portions within section elements for content of a single topic.
                        Finally, the <strong>nav</strong> element is used to bring a user to other pages or resources, depending on the destination
                        specified. Some of the different types of links this element creates are specified below.
                    </p>
                    <ol>
                        <li>External Link: An <strong>external anchor</strong> element creates a hyperlink to a URL of another website.</li>
                        <li>Internal Link: An <strong>internal anchor</strong> element creates a hyperlink to text within the same page.
                            This linked text has a reference, which the anchor element specifies in the ID attribute.  </li>
                        <li>Page-to-page: Some anchors are designed to resemble buttons and are typically utilized to navigate to another page
                            or resource within the same website.
                        </li>
                    </ol>
            </article>
            <article id="optimizingImages">
                <h3>OPTIMIZING IMAGES</h3>
                    <p>
                        When an image is fully optimized for a website, it will possess the following qualities:
                        It will have a <strong>descriptive file name</strong> for search engine optimization. Clearly describing the contents of
                        the image in its file name improves the chances that search engines will be able to categorize the file properly when returning 
                        image results for users. Keeping the file name concise also maintains the elements of the site organized.
                        Further, to load quickly, the images must have a <strong>small file size</strong>, the <strong>exact dimensions</strong> as required, and
                        if necessary, a reduced resolution. Larger file sizes will cause the load times for the site to get longer and could potentially impact its usability. 
                        For this reason, utilizing the appropriate image compression is important. Similarly, cropping or reducing the image resolution will
                        result in efficient site load times and maintain a high level of usability. An understanding of the  <strong>correct file formats</strong> 
                        and <strong>color modes</strong> to employ based on the type of image being displayed will help to display the images properly
                        and promptly.
                    </p>
                    <p>
                        The optimal file formats for displaying line art include <strong>GIF</strong> and <strong>PNG</strong>. GIFs are saved in indexed 
                        color mode and can be used to display animations, while PNG is usually saved in RGB color mode and has true transparency. 
                        <strong>WebP</strong>, and <strong>JPG</strong> are best suited for displaying photographic images and for this reason, are not typically used
                        for other types of content. JPG and WebP utilize lossy compression to make the file size of the image smaller, and the latter can display transparent 
                        backgrounds. <strong>SVG</strong>, or Scalable Vector Graphics, offers lossless compression as they are not made up of pixels as JPG or PNG are but rather, 
                        as the name suggests, of vector graphics marked with XML for two-dimensional, animated, or interactive images. 
                    </p>
            </article>
            <article id="favicons">
                <h3>FAVICONS</h3>
                    <p>
                        The browser will display a site-identifier image known as a <strong>favicon</strong> on the tab of the 
                        webpage being visited. It does so by loading and displaying the appropriate icon file, depending on what kind of browser the user is navigating the page with.
                        These files are typically ICO, PNG, or SVG files but can be saved as GIF files as well.
                        A user on a computer browser may require a larger-sized image to display, while a user on a cellphone would require the opposite. For this reason, favicons of
                        various different sizes of the icon are saved with the website's elements.
                        The request is made for the favicon file that the link specifies to display, and that image file is displayed in the browser
                        tab and when added to the smartphone's home screen.
                    </p>
            </article>
            </>
      );
}
export default TopicsPage;