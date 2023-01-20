# Raspberry Pi Dice

A simple, undistributed, Python package that acts as a die.
Essentially, it's a random number generator (RNG) that can be used for multiple purposes. However, this package was created as a side-project aiming to create a fairly simple dice rolling application for the Raspberry Pi Sense Hat.

## Getting started

### Examples

Take a look at the [examples](examples/) for a few implementation ideas.

### Unit testing

In order to run automated tests, execute:

```
python -m unittest
```

### Build

You can automatically create a `dist` folder by running the following script:

```
python -m build
```

The contents of the `dist` folder can be uploaded to the Python Package Index (pypi). Follow [this guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/#uploading-the-distribution-archives) in order to do so. Currently, this code is _not_ distributed.

## Roadmap

- Rolling a color die, with default and configurable colors
- Rolling a die with more than six sides, with text display instead of LED images.

## Notes

This project was created both to learn something and to scratch a personal itch. If you like it, or have any issues with it, feel free to [reach out by email](mailto:info@frisfruitig.com)!