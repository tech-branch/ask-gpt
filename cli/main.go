package main

import (
	"context"
	"fmt"
	"log"
	"os"
	"strconv"

	"github.com/PullRequestInc/go-gpt3"
	"github.com/joho/godotenv"
)

func main() {

	// load .env file if it exists
	godotenv.Load()

	// ------------
	//  Parameters
	// ------------

	tokens := 30
	temperature := 0.7
	engine := "text-davinci-003"

	// -----------
	//  Overrides
	// -----------

	maxTokens := os.Getenv("OPENAI_MAX_TOKENS")
	if maxTokens != "" {
		// convert string maxTokens to int tokens
		itokens, err := strconv.Atoi(maxTokens)
		if err != nil {
			log.Fatalln(err)
		}
		tokens = itokens
	}

	strTemp := os.Getenv("OPENAI_TEMPERATURE")
	if strTemp != "" {
		// convert string Temperature to float Temperature
		fTemp, err := strconv.ParseFloat(strTemp, 32)
		if err != nil {
			log.Fatalln(err)
		}
		temperature = fTemp
	}

	model := os.Getenv("OPENAI_MODEL")
	if model != "" {
		engine = model
	}

	// ------------
	//  API Config
	// ------------

	apiKey := os.Getenv("OPENAI_API_KEY")
	if apiKey == "" {
		log.Fatalln("Missing API KEY, set OPENAI_API_KEY environment variable or use the .env file")
	}

	ctx := context.Background()
	client := gpt3.NewClient(apiKey)

	// read prompt from the command line argument
	prompt := os.Args[1]

	response, err := client.CompletionWithEngine(ctx,
		engine,
		gpt3.CompletionRequest{
			Prompt:      []string{prompt},
			MaxTokens:   gpt3.IntPtr(tokens),
			Temperature: gpt3.Float32Ptr(float32(temperature)),
		},
	)
	if err != nil {
		log.Fatalln(err)
	}

	output := response.Choices[0].Text

	// --------------------
	//  Display the result
	// --------------------

	fmt.Println(output)
}
