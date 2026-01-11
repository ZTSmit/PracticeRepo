export async function helloThing(thing: string) {
    const response = await fetch(
        `http://localhost:8000/api/hello/${thing}`
    );

    if (!response.ok){
        throw new Error("Request failed");
    }

    return response.json() as Promise<{ output: string}>
}