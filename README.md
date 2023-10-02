# RouteWise (A submission for the Hacks-8.0 hackathon)

RouteWise is a a smart bus routing system, to optimize passenger inflow/outflow in city buses.

We've built machine learning algorithms to perform the optimization and a web app to provide information to our users.

## Machine Learning

For finding the optimal routes, we analyze city data.

[`src/routing/genetic_ml/genetics.ipynb`](src/routing/genetic_ml/genetics.ipynb) contains our genetic algorithm for finding optimal routes.\
[`src/routing/raw_network/routefinder_data.ipynb`](src/routing/raw_network/routefinder_data.ipynb) contains our code for normalizing and analyzing datasets containing city data.\
[`src/routing/raw_network/main.ipynb`](src/routing/raw_network/main.ipynb) contains our code for generating optimal bus stops from OpenStreetMap data.

1. We take note of the populations of each city area, and the number of people who travel from one area to another. Sources for this data are India's census', Google Maps and ride-sharing companies.
2. Once we have this data, we can establish the optimal bus stop locations throughout cities. This process takes place using graph manipulation. Different parts of the cities are represented as graph nodes.
3. Libraries such as `networkx`, `geopandas`, `osmnx`, `pandas`, `numpy` etc are used for this purpose.

Once we have optimal bus stops, we apply genetic algorithms with the reference bus stops, as well as existing bus stops.

The reason for choosing genetic algorithms is that we have a lot of different parameters to optimize.\
Things that need to be kept in mind are: refueling locations, route distance, alternative routes, crowd at locations, etc.
For optimizing multiple parameters, genetic algorithms are a great choice.

In genetic algorithms, we are creating approximate solutions which can maximize and minimize such parameters.
1. We generate an initial set of solutions through basic heuristics, and then these solutions are evaluated using a fitness function.
2. The fitness function looks at the parameters we want to optimize, and gives a score to each solution.
3. The solutions with the best scores are then selected, and they are used to generate new solutions.
4. This process is repeated until we get a solution which is good enough.

Once the process is completed, we have a set of routes which are optimal for the city.

## Web App

The web app is built using Bootstrap, HTML, CSS & JavaScript. It is hosted on Cloudflare Pages on a custom domain: <https://routewise.qwertys.tech>

It provides users with information on startup, and what we do.

## Our Team

- [Nikhil Dixit] - @nikhildixit27

