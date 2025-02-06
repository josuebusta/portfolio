
import React, { useState } from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';


import Navigation from './components/Navigation';
import './App.css';

import TopicsPage from './pages/TopicsPage.js';
import HomePage from './pages/HomePage.js';
import AlbumsPage from './pages/AlbumsPage.js';

import EditAlbumPageTable from './pages/EditAlbumPageTable';
import AddAlbumPageTable from './pages/AddAlbumPageTable';

function App() {

  const [album, setAlbumToEdit] = useState([]) 

  return (
    <>
      <BrowserRouter>

          <header>
          <img 
            src="android-chrome-192x192.png"
            alt="Josue Bustamante's Logo."
            title="© 2024 Josue Bustamante"
            />
          <h1>JOSUE BUSTAMANTE</h1>
          <p><strong>A portfolio website created to demonstrate proficiency with Mongoose, Express, React, and Node.js.</strong></p>
          </header>

          <Navigation />

          <main>
            <section>
                <Routes>
                  {/*<Route path="/" element={<AlbumsPage />} />*/}
                  <Route path="/" element={<HomePage />} />
                    {/* Add Routes for Home, Topics, Gallery, Contact, and Staff Pages.  */}
                    <Route path="/topics" element={<TopicsPage />} />
                    <Route path="/albums" element={<AlbumsPage setAlbum={setAlbumToEdit}/>} />
                 

                    <Route path="/create" element={<AddAlbumPageTable />} /> 
                    <Route path="/update" element={<EditAlbumPageTable albumToEdit={album} />} />

                    
                </Routes>
              </section>
          </main>

          <footer>
            <p>&#169; 2024 Josue Bustamante</p>
          </footer>

      </BrowserRouter>
    </>
  );
}

export default App;