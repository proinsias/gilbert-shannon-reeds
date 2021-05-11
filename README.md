# Gilbert-Shannon-Reeds

Python implementation of the Gilbert-Shannon-Reeds model for shuffling playing cards.

[![Mergify Status](https://img.shields.io/endpoint.svg?url=https://gh.mergify.io/badges/proinsias/gilbert-shannon-reeds&style=flat)](https://mergify.io)
[![License](https://img.shields.io/github/license/proinsias/gilbert-shannon-reeds.svg)](https://github.com/proinsias/gilbert-shannon-reeds/blob/master/LICENSE)
[![Cron Jobs](https://github.com/proinsias/gilbert-shannon-reeds/workflows/Cron%20Jobs/badge.svg)](https://github.com/proinsias/gilbert-shannon-reeds/actions/workflows/cronjobs.yml)
[![Pull Requests & Pushes](https://github.com/proinsias/gilbert-shannon-reeds/workflows/Pull%20Requests%20%26%20Pushes/badge.svg)](https://github.com/proinsias/gilbert-shannon-reeds/actions/workflows/pull-requests-and-pushes.yml)
[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit)

From Wikipedia:

> In the mathematics of shuffling playing cards,
> the Gilbert–Shannon–Reeds model is a probability distribution on riffle shuffle permutations
> that has been reported to be a good match for experimentally observed outcomes of human shuffling,
> and that forms the basis for a recommendation
> that a deck of cards should be riffled seven times in order to thoroughly randomize it.
>
> The deck of cards is cut into two packets...
> \[t\]hen, one card at a time is repeatedly moved
> from the bottom of one of the packets to the top of the shuffled deck.

Here we implement the Gilbert–Shannon–Reeds model, and verify this recommendation of seven shuffles.
