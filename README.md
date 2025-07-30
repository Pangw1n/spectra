# Spectra

**Spectra** is a Python program designed to plot transmittance vs. wavelength graphs for Transparent Conductive Oxides (TCOs). It supports plotting both single and combined graphs from your data files, making it easy to visualize and compare optical properties.

## Features

- Plot a single transmittance vs. wavelength graph from your data.
- Combine multiple datasets into a single graph for comparison.
- Simple command-line usage via Docker for portability and ease of setup.

## Usage

Spectra is distributed as a Docker container. You only need Docker installed, no Python environment setup required.

### 1. Single Graph Mode

To plot a single graph from your data:

```sh
docker run \
    -v path-to-input-directory:/input \
    -v path-to-output-directory:/output \
    spectra
```

- Replace `path-to-input-directory` with the path containing your input data files.
- Replace `path-to-output-directory` with the path where you want the output graph(s) saved.

### 2. Combined Graphs Mode

To plot multiple datasets on a single combined graph:

```sh
docker run \
    -v path-to-input-directory:/input \
    -v path-to-output-directory:/output \
    spectra --combine_graphs
```

## Input Data Format

- Input files should be placed in the `/input` directory (mounted from your host).
- Each file should contain wavelength and transmittance data, typically in CSV or TXT format.
- Ensure your files are formatted as expected by the program (see documentation or examples if provided).

## Output

- Output graphs will be saved in the `/output` directory (mounted from your host).
- File formats for output graphs are typically PNG or PDF.

## Example

```sh
docker run -v $(pwd)/data:/input -v $(pwd)/results:/output spectra
```

## License

This project is licensed under the MIT License.

## Support

For issues or feature requests, please open an issue in the repository.
