import React, { useState } from 'react';
import { useNavigate } from "react-router-dom";


export const AddAlbumPageTable = () => {

    const [title, setTitle]       = useState('');
    const [releaseDate, setReleaseDate]  = useState('');
    const [artist, setArtist] = useState('');
    const [ranking, setRanking] = useState('');
    
    const redirect = useNavigate();

    const addAlbum = async () => {
        const newAlbum = { title, releaseDate, artist, ranking };
        const response = await fetch('/albums', {
            method: 'post',
            body: JSON.stringify(newAlbum),
            headers: {
                'Content-Type': 'application/json',
            },
        });
        if(response.status === 201){
            alert(`Success! Your album is now part of the database.`);
        } else {
            const errMessage = await response.json();
            alert(` ${errMessage.Error} Error status ${response.status}. `);
        }
        redirect("/albums");
    };


    return (
        <>
            <h2>Add an album</h2>
            <p>Please add a new music album to your database by inputting the following: <br></br>
                The album's title, artist, release date, and its number in your personal 
                ranking of albums in your database.
            </p>
            
            <table id="albums">
                <caption>What album would you like to add?</caption>
                <thead>
                    <tr>
                        <th>Title</th>
                        <th>Artist</th>
                        <th>Release Date</th>
                        <th>Ranking</th>
                        <th></th>
                    </tr>
                </thead>
                <tbody>
                <tr>
                <td><label for="title" class="required">Album title</label>
                        <input
                            type="text"
                            placeholder="Title of the album"
                            value={title}
                            onChange={e => setTitle(e.target.value)} 
                            id="title" />
                    </td>

                    <td><label for="artist" class="required">Album artist</label>
                        <input
                            type="text"
                            placeholder="Album artist name"
                            value={artist}
                            onChange={e => setArtist(e.target.value)} 
                            id="artist" />
                    </td>

                    <td><label for="releaseDate" class="required">Release Date</label>
                        <input
                            type="date"
                            value={releaseDate}
                            placeholder="Release date of the album"
                            onChange={e => setReleaseDate(e.target.value)} 
                            id="releaseDate" />
                    </td>

                    <td><label for="ranking" class="required">Ranking</label>
                        <input
                            type="number"
                            placeholder="User's ranking"
                            value={ranking}
                            onChange={e => setRanking(e.target.value)} 
                            id="ranking" />
                    </td>

                    <td>
                    <label for="submit">Save Album</label>
                        <button
                            type="submit"
                            onClick={addAlbum}
                            id="submit"
                        >Add</button>
                    </td>
                </tr>
                </tbody>
            </table>
    </>
);
}

export default AddAlbumPageTable;