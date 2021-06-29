// import postgres
const { Client } = require('pg')

// main function
async function main() {	
	// client
	const client = new Client({
		user: "dev1",
		password: "password",
		host: "10.0.0.53",
		database: "db1",
		port: 5432
	})
	await client.connect()

	// dude that's crazy
	const res = await client.query('SELECT * FROM test;')
	console.log(res.rows)

	// dude what's up dude
	await client.end()
}

// async function
main()