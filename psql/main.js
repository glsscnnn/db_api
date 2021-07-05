// import postgres
const { Client } = require('pg')

// customize create record
const create = async (client, table_name) => { }

const update = async () => {
	// update the client
}

const read = async (client, rows, table) => {
	// connect to client then query
	await client.connect()
	const res = await client.query(`SELECT ${rows} FROM ${table}`)

	// close the connection
	await client.end()

	// return the rows
	return res.rows
}

const del = async () => {

}

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