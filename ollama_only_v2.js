/**
 * JavaScript implementation for extracting structured pet data from text using Ollama.
 * Uses Zod for schema validation and type safety.
 */
import ollama from 'ollama';
import { z } from 'zod';
import { zodToJsonSchema } from 'zod-to-json-schema';

// Define the schema using Zod
const Pet = z.object({
    name: z.string(),
    animal: z.string(),
    age: z.number(),
    color: z.string().nullable(),
    favorite_toy: z.string().nullable(),
});

const PetList = z.object({
    pets: z.array(Pet),
});

async function extractPetData() {
    try {
        const response = await ollama.chat({
            model: 'llama3.2:latest',
            messages: [{
                role: 'user',
                content: `
                    I have two pets.
                    A cat named Luna who is 5 years old and loves playing with yarn. She has grey fur.
                    I also have a 2 year old black cat named Loki who loves tennis balls.
                `
            }],
            format: zodToJsonSchema(PetList),
        });

        // Parse and validate the response using Zod
        const petData = PetList.parse(JSON.parse(response.message.content));
        console.log('Extracted Pet Data:', JSON.stringify(petData, null, 2));

        return petData;
    } catch (error) {
        console.error('Error:', error);
        throw error;
    }
}

// Run the example
extractPetData();
