function HomePage() {
    return (
        <>
        <h2>HOME</h2>
        <article>
            <p>
            My career goals towards pursuing AI engineering include finishing my Computer Science postbaccalaureate degree, 
                obtaining certifications centered around AI, and acquiring an internship in the industry to gain practical experience.
                Having just recently begun my education in Computer Science after working in a liberal arts field for a decade,
                I am excited to be in a program that not only provides rigorous training but also the opportunity to connect and collaborate
                with my peers, even on an online model. I feel that when I graduate from the program in the next year, I will have received
                a solid foundation upon which I can seek out further instruction. AI as a field in Computer Science is developing and evolving
                rapidly, and continuing my education beyond this program through certifications or advanced degrees will allow me to be better
                prepared once seeking out employment. I aspire to receive an opportunity for such an employment through completion of an 
                internship program in which I can delve into further experience and build a network of peers in the field. Knowing how 
                competitive the career landscape is at the moment drives me to make the most of my studies and work hard to find my place in
                a career field I am becoming progressively more enamored and fascinated by.
            </p>
            <p>
                    <dl>
                        <dt>CRUD</dt>
                        <dd>
                            Create, Read, Update, and Delete. The four data processes implemented in database management. The elements in this database can be
                            constructed or erased, and the information thereof can be processed and / or modified. Therefore, it can perform CRUD operations on
                            data.
                        </dd>
                        <dt>MongoDB</dt>
                        <dd>
                            A document-oriented database management system with capabilities to perform CRUD operations on data: Create, Read, Update, Delete.
                            This type of system stores data internally in JSON-like documents known as BSON, or Binary JSON. It does not support Structured Query Language, 
                            differentiating it from Relational Databases. Depending on the needs of the database, this system is used in website applications and 
                            managing website content. It is used in this website to organize and manage the data for album elements containing titles, artist names,
                            release dates, and rankings.
                        </dd>
                        <dt>HTML</dt>
                        <dd>
                            HyperText Markup Language. This language is used to create webpages and web applications, specifying a structure by way of elements, their tags, and how
                            they are nested within each other. It also defines the appearance and functions of a webpage through the use of attributes added onto the tags. In order
                            to write this text, I am currently manipulating the text of a JSON file, which utilizes HTML-like nesting to dictate its structure.
                        </dd>
                        <dt>DOM</dt>
                        <dd>
                            The Document Object Model, which is a representation of the structure of a webpage, typically written in HTML. It is formed when a browser interprets the data
                            of a document into a hierarchical tree of nodes, each node representing a document, document type, element, attribute, or piece of text. It is based on this
                            interpretation that the browser then displays the rendition in the viewport. The user is currently reading text being displayed in the viewport after
                            the document it is written to was interpreted by the browser for the final display.
                        </dd>
                        <dt>JavaScript</dt>
                        <dd>
                            A programming language for web development which is utilized to create a more dynamic and interactive interface for the user. It does so by manipulating
                            the Document Object Model tree in response to a user's input or action events. The instantaneous changes that can be made to this website's database, 
                            performing CRUD operations through clicking or other input, is facilitated by JavaScript programming.
                        </dd>
                        <dt>Asynchronous Programming</dt>
                        <dd>
                            Instead of the default synchronous programming that JavaScript operates under wherein any line of code can block the program, asynchronous functions do not
                            need to wait for a task to finish before moving on to the next. Instead, the next tasks can be executed while the asynchronous process is completed. These
                            types of functions are facilitated using promises to access the function's result and async/await to chain the function calls. The database implementation
                            in the webpage utilizes asynchronous programming to handle the status messages received after a request.
                        </dd>
                        <dt>CSS</dt>
                        <dd>
                            Cascading Style Sheets, used to design the presentation of HTML documents through the specification of colors, fonts, images, etc. A stylesheet is typically
                            externally linked to be imported into a site's webpages as the global style. This website uses an App.css file to outline the overall presentation of every 
                            page in order to present a cohesive product. 
                        </dd>
                        <dt>Node.js</dt>
                        <dd>
                            A JavaScript runtime environment for developing applications on the server side. Its Node Package Manager offers open-source, third-party modules and packages
                            to install from its online repository. The JavaScript program being run on this website was developed using Node.js and is dependent on packages acquired
                            through the Node Package Manager.
                        </dd>
                        <dt>Express</dt>
                        <dd>
                            A framework for creating Node.js web applications. It contributes the capability to specify routes for data requests and responses through Application Programming
                            Interfaces. As a result, the application is able to perform get, post, and delete processes on data. Further, Express can add middleware to its request and response 
                            routes for enhanced processes and features. The CRUD operations performed on the database in this website are possible through the get, post, and delete capabilities
                            of Express. The response to requests for these operations signal whether a process was successful or if an error must be handled.
                        </dd>
                        <dt>React</dt>
                        <dd>
                            A framework for creating a webpage's user interface and frontend applications. React applications are component-based as opposed to static HTML. These components
                            are reusable functions written in JSX, a syntax which incorporates HTML in JavaScript. With these capabilities, React can create Single Page Applications, which negates
                            the need for multiple HTML pages and sends the site's data from the server to the browser only once. The DOM tree is updated on the client-side as opposed to server-side
                            for increased efficiency. The components present in this website include Album.js to display an album in the database, AlbumList.js to display the complete collection,
                            and Navigation.js to redirect from webpage to webpage.
                        </dd>
                        <dt>SPA</dt>
                        <dd>
                            Single Page Application, used in place of multiple HTML pages. This concept is utilized in the React framework, where the majority of information is sent from the server to 
                            the browser during the initial loading of the webpage. Any changes to the DOM is made asynchronously using JavaScript to give the dynamic impression that the user is
                            navigating to different pages on the site without requiring another page load. This website utilizes this procedure by having the Home Page, Topics Page, and Albums pages
                            as components to be rendered by the SPA.
                        </dd>
                        <dt>REST</dt>
                        <dd>
                            Representational State Transfer, an architectural style for web services. This style performs CRUD operations using HTTP methods to access resources within collections. 
                            It is stateless, and each request for a resource requires all information needed to process the request to be present at once. This website utilizes the REST style
                            when making requests for the elements in the database to manipulate the data.
                        </dd>
                    </dl>
                </p>
        </article>
        </>
    );
}
export default HomePage;