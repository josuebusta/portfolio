import React, { useState }  from 'react';
import { useNavigate } from "react-router-dom";

export const EditAlbumPageTable = ({ albumToEdit }) => {
 
    const [title, setTitle]       = useState(albumToEdit.title);
    const [artist, setArtist] = useState(albumToEdit.artist);
    const [releaseDate, setReleaseDate]  = useState(albumToEdit.releaseDate.slice(0,10));
    const [ranking, setRanking] = useState(albumToEdit.ranking);
    
    const redirect = useNavigate();

    const editAlbum = async () => {
        const response = await fetch(`/albums/${albumToEdit._id}`, {
            method: 'PUT',
            body: JSON.stringify({ 
                title: title,
                artist: artist,
                releaseDate: releaseDate,
                ranking: ranking
            }),
            headers: {'Content-Type': 'application/json',},
        });

        if (response.status === 200) {
            alert(`Success! Changes to "${title}" have been saved.`);
        } else {
            const errMessage = await response.json();
            alert(`Something went wrong: ${response.status}. ${errMessage.Error}`);
        }
        redirect("/albums");
    }

    return (
        <>
            <h2>Edit an album</h2>
            <p>Edit an existing album in your database by changing any of the values below.<br></br>
                The album's current information is displayed
                by default.
            </p>
            <table id="albums">
                <caption>Change the desired information.</caption>
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
                <td><label for="title">Album title</label>
                        <input
                            type="text"
                            placeholder="Title of the album"
                            value={title}
                            onChange={e => setTitle(e.target.value)} 
                            id="title" />
                    </td>

                    <td><label for="title">Album artist</label>
                        <input
                            type="text"
                            placeholder="Album artist name"
                            value={artist}
                            onChange={e => setArtist(e.target.value)} 
                            id="artist" />
                    </td>

                    <td><label for="releaseDate">Release Date</label>
                        <input
                            type="date"
                            value={releaseDate}
                            placeholder="Release date of the album"
                            onChange={e => setReleaseDate(e.target.value)} 
                            id="releaseDate" />
                    </td>

                    <td><label for="ranking">Ranking</label>
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
                            onClick={editAlbum}
                            id="submit"
                        >Submit</button>
                    </td>
                </tr>
                </tbody>
            </table>
        </>
    );
}
export default EditAlbumPageTable;