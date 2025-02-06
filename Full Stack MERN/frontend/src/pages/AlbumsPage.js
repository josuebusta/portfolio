import { React, useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';

import AlbumList from '../components/AlbumList';
import { Link } from 'react-router-dom';
import { MdAlbum } from "react-icons/md";

function AlbumsPage({ setAlbum }) {
    // Use the Navigate for redirection
    const redirect = useNavigate();

    // Use state to bring in the data
    const [albums, setAlbums] = useState([]);

    // RETRIEVE the entire list of albums
    const loadAlbums = async () => {
        const response = await fetch('/albums');
        const albums = await response.json();
        setAlbums(albums);
    } 
    

    // UPDATE a single album
    const onEditAlbum = async album => {
        setAlbum(album);
        redirect("/update");
    }


    // DELETE a single album  
    const onDeleteAlbum = async _id => {
        const response = await fetch(`/albums/${_id}`, { method: 'DELETE' });
        if (response.status === 200) {
            const getResponse = await fetch('/albums');
            const albums = await getResponse.json();
            setAlbums(albums);
        } else {
            console.error(`The album with the ID ${_id} could not be deleted. This error was raised: ${response.status}`)
        }
    }

    // LOAD all the albums
    useEffect(() => {
        loadAlbums();
    }, []);

    // DISPLAY the albums
    return (
        <>
            <h2>Albums</h2>
            <p><strong>View</strong> the list of albums in your database. <br></br>
                <strong>Add</strong> an album to the list by clicking on the link below.<br></br>
                <strong>Remove</strong> an album by clicking on the delete button in its row. <br></br>
                <strong>Edit</strong> an album's information by clicking on the respective edit button.
            </p>
            <Link to="/create"> <MdAlbum /> Add Album</Link>
            <AlbumList 
                albums={albums} 
                onEdit={onEditAlbum} 
                onDelete={onDeleteAlbum} 
            />
        </>
    );
}

export default AlbumsPage;