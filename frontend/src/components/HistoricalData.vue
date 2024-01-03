<template>
    <div id="table-container">
        <h1>Logs</h1>

        <div id="logs-container">
            <table>
                <th>Date and Time</th>
                <th>Turbidity</th>
                <th>Humidity</th>
                <th>TDS</th>

                <tr>
                    <td>12 / 10 / 2023 11:40AM</td>
                    <td>10.4</td>
                    <td>19</td>
                    <td>23</td>
                </tr>
                
                
            </table>
        </div>
    </div>
</template>

<script>
export default {
    name: 'HistoricalData',
    methods: {
        async retrieve_data(){
        }
    },
    data() {
        return {
            'logs': []
        }
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
        background-color: #e9e9e9;
    }
}
</style>