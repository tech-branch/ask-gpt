# OpenAI Model Communication

This project provides a convenient way to communicate with OpenAI models through various interfaces. The following methods are currently supported:

## Command-line executable

Run the cli tool and enter your queries directly in the terminal.

```bash
./ask-gpt "Why trees have so many branches?"
```

## Alfred workflow

Use the provided Alfred workflow to quickly access the model and input your queries without leaving your current application.

Simple answer:

```
qa Why trees have so many branches?
```

More expensive answer:

```
qal Why trees have so many branches?
```


## Installation

- Clone the repository to your local machine.

### Alfred workflow:

- Install `requests` using `python3 -m pip install requests`
- `Cmd+click` the `.alfredworkflow` file and follow the instructions in the config step. You'll have to supply your OpenAI API key.

### Executable

Build it yourself with the Golang build tool:

```
cd cli
go build
```
