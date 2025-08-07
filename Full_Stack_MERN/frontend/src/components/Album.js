import React from 'react';

import { RiDeleteBin7Fill, RiEditBoxFill } from 'react-icons/ri';


function Album({ album, onEdit, onDelete }) {
    return (
        <tr>
            <td>{album.title}</td>
            <td>{album.artist}</td>
            <td>{album.releaseDate.slice(0,10)}</td>
            <td>{album.ranking}</td>

            <td><RiDeleteBin7Fill onClick={() => onDelete(album._id)} /></td>
            <td><RiEditBoxFill onClick={() => onEdit(album)} /></td>
        </tr>
    );
}

export default Album;