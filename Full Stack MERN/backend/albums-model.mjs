// Models for the Album Collection

import mongoose from 'mongoose';
import 'dotenv/config';

// Connect based on the .env file parameters.
mongoose.connect(
    process.env.MONGODB_CONNECT_STRING,
    { useNewUrlParser: true }
);
const db = mongoose.connection;

// Confirm that the database has connected and print a message in the console.
db.once("open", (err) => {
    if(err){
        res.status(500).json({ Error: 'Oh no! There was an error with the server.' });
    } else  {
        console.log('Success! You are now connected to the music library database!');
    }
});

// SCHEMA: Define the collection's schema.
const albumSchema = mongoose.Schema({
	title:    { type: String, required: true },
	releaseDate: { type: Date, required: true, default: Date.now },
	artist: { type: String, required: true },
    ranking: { type: Number, required: true}
});

// Compile the model from the schema 
// by defining the collection name "albums".
const albums = mongoose.model('Albums', albumSchema);


// CREATE model *****************************************
const createAlbum = async (title, releaseDate, artist, ranking) => {
    const album = new albums({ 
        title: title, 
        releaseDate: releaseDate, 
        artist: artist, 
        ranking: ranking
    });
    return album.save();
}


// RETRIEVE model *****************************************
// Retrieve all documents and return a promise.
const retrieveAlbums = async () => {
    const query = albums.find();
    return query.exec();
}

// RETRIEVE by ID
const retrieveAlbumByID = async (_id) => {
    const query = albums.findById({_id: _id});
    return query.exec();
}

// DELETE model based on _id  *****************************************
const deleteAlbumById = async (_id) => {
    const result = await albums.deleteOne({_id: _id});
    return result.deletedCount;
};


// UPDATE model *****************************************************
const updateAlbum = async (_id, title, releaseDate, artist, ranking) => {
    const result = await albums.replaceOne({_id: _id }, {
        title: title,
        releaseDate: releaseDate,
        artist: artist,
        ranking: ranking
    });
    return { 
        _id: _id, 
        title: title,
        releaseDate: releaseDate,
        artist: artist,
        ranking: ranking 
    }
}

// EXPORT the variables for use in the controller file.
export { createAlbum, retrieveAlbums, retrieveAlbumByID, updateAlbum, deleteAlbumById }