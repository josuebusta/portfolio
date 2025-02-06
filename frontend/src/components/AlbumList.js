import React from 'react';
import Album from './Album';

function AlbumList({ albums, onDelete, onEdit }) {
    return (
        <table id="albums">
            <caption>Add, Edit, and Delete Albums</caption>
            <thead>
                <tr>
                    <th>Title</th>
                    <th>Artist</th>
                    <th>Release Date</th>
                    <th>Ranking</th>
                    <th>Delete</th>
                    <th>Edit</th>
                </tr>
            </thead>
            <tbody>
                {albums.map((album, i) => 
                    <Album 
                        album={album} 
                        key={i}
                        onDelete={onDelete}
                        onEdit={onEdit} 
                    />)}
            </tbody>
        </table>
    );
}

export default AlbumList;
