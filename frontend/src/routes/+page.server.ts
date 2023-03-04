import type { PageServerLoad } from "./$types";

export async function load(req: PageServerLoad) {
    return {
        test: 'Hello World!'
    }
}