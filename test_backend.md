#Projet Dreem - Backend


## Idea

Build a backend server able to store, download and upload data recorded from the Dreem headband. Set up asynchroneous tasks to parse this data and an API to access it.

## Details


- A record is generated when a user wears a device during a night.
- A record is an H5 file with meta-data in it. Meta-data are listed in the H5 file.
- Devices are shared: they can be worn by different users.
- A user can make several records with different devices.

## Specifications

- Build an API with the access to the following ressources: record, device, user
- Schedule a task when a record is uploaded to parse its metadata and store it in a SQL database.
- Build a minimum front-end based on this API to display this data, download the data, and upload new data files.
- Add an endpoint to access the signal of a record between two arbitrary timestamps

## Data

The data given with this test are 4 HDF5 files (`record1.h5`, `record2.h5`, `record3.h5`, `record4.h5`). These files contain data recorded by the device during a night. The device is composed by N electrods (Usually 4). They produce data listed in the h5 file as channel1, channel2, channelN .. For each channel there is 3 arrays: raw data, filtered data, and impedance data. Raw data is the most useful.

Moreover you'll find a number of metadata in this file such as the start time, stop time, sleep score, number of stimulations, hypnogram, etc. These are the information that needs to be stored in a relational database.


## Bonus

- Add a user permission layer
- Add filters on the routes (for instance, get all the records for a specific user with one request)
- Unit tests
- Monitor the asynchroneous task pipeline
- Dockerfile

## Technologies
- Python and Django
- Django rest framework is advised for building the API
- Git for the versionning
- No frontend library is imposed

## Deliverable

Please give us access to a Git repository with the code.
