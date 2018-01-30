data = {
    "artists": [
      {
        "artistName": "Lupe Fiasco",
        "artistsPicture": "../assets/artists-images/lupe.jpg",
        "genre": "Hip-Hop",
        "albums": [
          { "name": "Food & Liquor",
            "albumCover": "../assets/album-covers/f&l.jpg",
            "songs": {
              "name": "Kick, Push",
              "file": "mp3"
            }
          }
        ]
      },
      {
        "artistName": "Flume",
        "artistsPicture": "../assets/artists-images/flume.jpg",
        "genre": "",
        "albums": [
          { "name": "Flume",
            "albumCover": "../assets/album-covers/flume.jpg",
            "songs": {
              "name": "Sleepless",
              "file": "mp3"
            }
          },
          { "name": "Skin",
            "albumCover": "../assets/album-covers/skin.png",
            "songs": {
              "name": "Sleepless",
              "file": "mp3"
            }
          }
        ]
      },
      {
        "artistName": "Linkin Park",
        "artistsPicture": "../assets/artists-images/linkinpark.jpg",
        "genre": "",
        "albums": [
          { "name": "Hybrid Theory",
            "albumCover": "../assets/album-covers/meteora.jpg",
            "songs": {
              "name": "Sleepless",
              "file": "mp3"
            }
          }
        ]
      },
      {
        "artistName": "Drake",
        "artistsPicture": "../assets/artists-images/drake.jpg",
        "genre": "",
        "albums": [
          { "name": "Views",
            "albumCover": "../assets/album-covers/views.png",
            "songs": {
              "name": "Sleepless",
              "file": "mp3"
            }
          }
        ]
      },
      {
        "artistName": "J.Cole",
        "artistsPicture": "../assets/artists-images/jcole.jpg",
        "genre": "",
        "albums": [
          { "name": "2014 Forest Hills Drive",
            "albumCover": "../assets/album-covers/fhd.jpg",
            "songs": {
              "name": "Sleepless",
              "file": "mp3"
            }
          }
        ]
      },
      {
        "artistName": "Eminem",
        "artistsPicture": "../assets/artists-images/eminem.jpg",
        "genre": "",
        "albums": [
          { "name": "Marshal Matthers LP",
            "albumCover": "../assets/album-covers/mmlp.jpg",
            "songs": {
              "name": "Sleepless",
              "file": "mp3"
            }
          }
        ]
      },
    ]
  }

const albums = data.artists.reduce((acc, next) => {
  next.albums.forEach(album => {
    acc.push(album);
  });
  return acc;
}, []);

console.log('albums: ', albums);
