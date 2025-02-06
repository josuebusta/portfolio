// Controllers for the Album Collection

import 'dotenv/config';
import express from 'express';
import * as albums from './albums-model.mjs';

const PORT = process.env.PORT;
const app = express();
app.use(express.json());  // REST needs JSON MIME type.


// CREATE controller ******************************************
app.post ('/albums', (req,res) => { 
    albums.createAlbum(
        req.body.title, 
        req.body.releaseDate, 
        req.body.artist,
        req.body.ranking
        )
        .then(album => {
            console.log(`Success! "${album.title}" is now part of the database.`);
            res.status(201).json(album);
        })
        .catch(error => {
            console.log(error);
            res.status(400).json({ Error: 'Oh no! Failed to add album to the database.' });
        });
});


// RETRIEVE controller ****************************************************
app.get('/albums', (req, res) => {
    albums.retrieveAlbums()
        .then(albums => { 
            if (albums !== null) {
                console.log(`Success! All albums have been retrieved from the database.`);
                res.json(albums);
            } else {
                res.status(404).json({ Error: 'Hmm, that album was not found.' });
            }         
         })
        .catch(error => {
            console.log(error);
            res.status(400).json({ Error: 'Oh no! Failed to retrieve albums.' });
        });
});


// RETRIEVE by ID controller
app.get('/albums/:_id', (req, res) => {
    albums.retrieveAlbumByID(req.params._id)
    .then(album => { 
        if (album !== null) {
            console.log(`Success! The ID was matched and "${album.title} was retrieved.`);
            res.json(album);
        } else {
            res.status(404).json({ Error: 'Hmm, that album was not found.'});
        }         
     })
    .catch(error => {
        console.log(error);
        res.status(400).json({ Error: 'Oh no! Failed to retrieve album.' });
    });

});


// UPDATE controller ************************************
app.put('/albums/:_id', (req, res) => {
    albums.updateAlbum(
        req.params._id, 
        req.body.title, 
        req.body.releaseDate, 
        req.body.artist,
        req.body.ranking
    )
    .then(album => {
        console.log(`Success! The information for "${album.title}" was updated.`);
        res.json(album);
    })
    .catch(error => {
        console.log(error);
        res.status(400).json({ Error: 'Oh no! Failed to update album.' });
    });
});


// DELETE Controller ******************************
app.delete('/albums/:_id', (req, res) => {
    albums.deleteAlbumById(req.params._id)
        .then(deletedCount => {
            if (deletedCount === 1) {
                console.log(`Based on its ID, ${deletedCount} album was deleted.`);
                res.status(200).send({ Success: 'The album was deleted.' });
            } else {
                res.status(404).json({ Error: 'Hmm, that album was not found.' });
            }
        })
        .catch(error => {
            console.error(error);
            res.send({ Error: 'Oh no! Failed to delete album.' });
        });
});


app.listen(PORT, () => {
    console.log(`Server listening on port ${PORT}...`);
});