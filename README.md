# demo-snow-cloud

## Service template

In this service template (**service.yaml**), the following is created:

- OpenStack Security Group and Keypair
- 2 OpenStack VMs
- Docker host
- Docker network
- Docker Registry certificates to access private SODALITE image registry
- SODALITE Snow UC components
- NiFi instance
- Data pipeline that moves output images into an S3 bucket
- AWS Lambda serverless function that generates thumbnails out of these output images and moves to another S3 bucket 

### Prerequisites

In order to run the test service, the following packages are needed:

- openstack==0.52
- xOpera

Additionally, the following sister directories must exist:

```
$ tree -L 1
.
├── demo-snow-cloud <- this repository
├── iac-modules
└── ThumbnailGeneration

```

- **iac-modules**: `git clone https://github.com/RADON-SODALITE/iac-modules`
- **ThumbnailGeneration**: an extracted and merged CSAR of these service templates: [ThumbnailGeneration](https://github.com/RADON-SODALITE/radon-particles/blob/master/servicetemplates/radon.blueprints/ThumbnailGeneration/ServiceTemplate.tosca) and [DataPipelineExample](https://github.com/RADON-SODALITE/radon-particles/blob/master/servicetemplates/radon.blueprints.examples/DataPipelineExample/ServiceTemplate.tosca). Once extracted, the files in the `\_definitions` directory should be modified pointing to relative path for node and relationship types, e.g. 
    - `/nodetypes/radon.nodes.nifi/Nifi/files/stop/stop.yml -> ../nodetypes/radon.nodes.nifi/Nifi/files/stop/stop.yml`
    - `/relationshiptypes/radon.relationships.datapipeline/ConnectNifiLocal/files/connect.yml -> ../relationshiptypes/radon.relationships.datapipeline/ConnectNifiLocal/files/connect.yml`

### Deployment

To prepare needed node and relationship types, run:
```
$ make prepare
```

To deploy, firstly modify **input.yaml** and then run:
```
$ make deploy
```

## Test service

In this test service (**test_service.yaml**), the following is created:

- OpenStack Security Group and Keypair
- OpenStack VM
- Docker host
- Docker network
- Simple text file
- NiFi instance
- Data pipeline that moves the text file in S3 bucket

### Prerequisites

In order to run the test service, the following packages are needed:

- openstack==0.52
- xOpera

Additionally, the following sister directories must exist:

```
$ tree -L 1
.
├── demo-snow-cloud <- this repository
├── iac-modules
└── localToS3Pipeline

```

- **iac-modules**: `git clone https://github.com/RADON-SODALITE/iac-modules`
- **localToS3Pipeline**: an extracted CSAR of this [DataPipelineExample](https://github.com/RADON-SODALITE/radon-particles/blob/master/servicetemplates/radon.blueprints.examples/DataPipelineExample/ServiceTemplate.tosca) service template. Once extracted, the files in the `\_definitions` directory should be modified pointing to relative path for node and relationship types, e.g. 
    - `/nodetypes/radon.nodes.nifi/Nifi/files/stop/stop.yml -> ../nodetypes/radon.nodes.nifi/Nifi/files/stop/stop.yml`
    - `/relationshiptypes/radon.relationships.datapipeline/ConnectNifiLocal/files/connect.yml -> ../relationshiptypes/radon.relationships.datapipeline/ConnectNifiLocal/files/connect.yml`

### Deployment

To prepare needed node and relationship types, run:
```
$ make prepare-test
```

To deploy, firstly modify **input.yaml** and then run:
```
$ make deploy-test
```