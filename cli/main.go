package main

import (
	"context"
	"fmt"
	"log"
	"os"

	"github.com/PullRequestInc/go-gpt3"
	"github.com/joho/godotenv"
)

func main() {
	godotenv.Load()

	apiKey := os.Getenv("OPENAI_API_KEY")
	if apiKey == "" {
		log.Fatalln("Missing API KEY, set OPENAI_API_KEY environment variable or use the .env file")
	}

	ctx := context.Background()
	client := gpt3.NewClient(apiKey)

	prompt := os.Args[1]

	resp, err := client.Completion(ctx, gpt3.CompletionRequest{
		Prompt:    []string{prompt},
		MaxTokens: gpt3.IntPtr(128),
	})
	if err != nil {
		log.Fatalln(err)
	}
	fmt.Println(resp.Choices[0].Text)
}
