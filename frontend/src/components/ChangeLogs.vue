<template>
    <div id="table-container">
        <h1>Deleted Logs</h1>

        <div id="logs-container">
            <table>
                <th>Date and Time</th>
                <th>Turbidity</th>
                <th>PH</th>
                <th>TDS</th>
                <th>Temperature</th>
                <th>Power Life</th>
                <th>Date Deleted</th>

                <tr v-for="log in logs" :key="log">
                    <td>{{ log.date_created }}</td>
                    <td>{{ log.turbidity }}NTU</td>
                    <td>{{ log.ph }}pH</td>
                    <td>{{ log.tds }}pn</td>
                    <td>{{ log.ec }}°C</td>
                    <td>{{ log.battery }}%</td>
                    <td>{{ log.date_deleted }}</td>
                </tr>
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name: 'ChangeLogs',
    methods: {
        async retrieve_data(){
            const response = await fetch(`https://aquaeasy.onrender.com/all_deleted_entries?user_id=${this.user_data.id}`);
            // const response = await fetch(`http://127.0.0.1:8000/all_deleted_entries?user_id=${this.user_data.id}`);
            const data = await response.json();

            if (!response.ok){
                console.log('Failed.');
            }
            else{
                this.logs = data.payload;
            }            
        }
    },
    props: {
        user_data: {}
    },  
    data() {
        return {
            logs: []
        }
    },
    mounted(){
        this.retrieve_data();
        
        setInterval(() => {
            this.retrieve_data();
        }, 70000)
    }
}
</script>

<style scoped lang="scss">
#table-container {
    height: 80%;
    width: 90%;
    display: flex;
    flex-direction: column;
}

#logs-container {
    height: 100%;
    width: 100%;
    border-radius: 15px;
    box-shadow: 2px 2px 5px #C9C9C9;
    overflow: auto; /* Add overflow: auto to enable scrolling if the content is larger than the container */

    table {
        width: 100%;
        border-collapse: collapse; /* Combine borders for adjacent cells */
    }

    th, td {
        padding: 10px;
        text-align: center;
        border: 1px solid #ccc;
    }

    th {
        background-color: #1497DD;
        color: white;
        border-collapse: collapse;
        border: none;
        position: sticky;
        top: 0;
    }
}
</style>