# SWESARR: SWE retrievals!

## Project Title and Introduction

Perform SWE retrievals on SnowEx SWESARR data using physically based algorithms. SWESARR (https://blogs.nasa.gov/swesarr/) is an airborne X+dual Ku (~10, 13, 17 GHz) SAR flown over the Grand Mesa and Alaska SnowEx sites in 2020 and 2024. This technology builds straight into orbit! At least five space agencies have considered these frequencies to make the first reliable spaceborne estimates of global snow. The SWESARR team including Dylan Boyd (who is leading a tutorial on SWESARR!) has been working hard since 2020 to create the normalized radar cross-section (σ0) datasets from the raw radar data. We are finally so very close to using SWESARR to really answer some of the most central motivating questions behind SnowEx.

The project will perform these retrievals using prototype, draft datasets, and the recently published BASE-AM algorithm (originally by my former student Jinmei Pan; read up on tower validation https://tc.copernicus.org/articles/18/1561/2024/tc-18-1561-2024.pdf and airborne validation https://tc.copernicus.org/articles/18/747/2024/).

### Collaborators

| Name | Personal goals | Can help with | Role |
| ------------- | ------------- | ------------- | ------------- |
| Mike D. | I want to get all the pieces set up to roll with SWESARR retrievals as soon as the SWESARR team makes data public| I can help with understanding retrieval algorithms and programming in Python  | Project Lead |
| ... | ... | ... | ... |
| ... | ... | ... | ... |

### The problem

There are not any simplem, global relationships between radar backscaatter and SWE. Thus has motivated many retrieval algorithms. Arguably, it is very valuable to use physically-based multi-layer approaches that can be compared as directly as possible with validation data. 

## Data and Methods

### Data

We have a single, draft SWESARR backscatter image. This is not final data but is the latest, greatest from Goddard.

### Existing methods

Most approaches have used single-layer algorithms (e.g. https://ieeexplore.ieee.org/abstract/document/8412144?casa_token=cToHs14akiAAAAAA:ssGop-rLj8o7mIaz9rQqiIZ2hHn0XbKiSPHo3jeHxeW8nzHTO_G9imy8Eh_go1PKzl60pSbGOgE) . These are useful but have limitations. For example, their estimate of snow microstructure is an effective one-layer single-scatter albedo, which cannot be meaningfully compared with in situ measurements of microstructure.

### Proposed methods/tools

We will use the recently published BASE-AM algorithm (originally by my former student Jinmei Pan; read up on tower validation https://tc.copernicus.org/articles/18/1561/2024/tc-18-1561-2024.pdf and airborne validation https://tc.copernicus.org/articles/18/747/2024/).

BASE-AM is a Markov Chain Monte Carlo method. Some use similar approaches for machine learning, but here we are not learning based on input/output relations but rather embedding a physically based model, more simiar conceptually to a physically-based approach based on objective function minimization

### Background reading

* Here's the TDS piece on MCMC https://towardsdatascience.com/monte-carlo-markov-chain-mcmc-explained-94e3a6c8de11


## Project goals and tasks

### Project goals

* Create a simple and extensible structure for doing BASE-AM runs
* Do runs at the snowpits, comparing output to available snowpit and soil measurements
* Do distributed runs and see an image of retrieved SWE

### Tasks

* Task 1 all team members will learn to use GitHub
* Task 2 team members will explore the SWESARR data using rioxarray
* Task 3 team members will explore the BASE-AM algorithm
* Task 4 build BASE-AM to SWESARR interface
* Task 5 strategy and implementation for BASE-AM runs at scale

## Project Results

Can't wait to see
