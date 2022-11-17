<template>
    <div class="table">
        <tr v-for="stock in stocks" :key="stock">
            <th>{{ stock.Name }}</th>
            <th>{{ stock.Value }}</th>
            <th>{{ stock.Change }}</th>
            <th>{{ stock.Date }}</th>
        </tr>
    </div>
</template>

<script>
import axios from 'axios';
import store from "../store";

export default {
    name: 'DashboardView',
    data() {
        return {
            stocks: [],
        }
    },
    methods: {
        async getStockData() {
            try {
                console.log(store.state.accessToken)
                console.log(store.state.expiration)

                await axios.get('broker/stock/', {
                    headers: {
                        'Authorization': store.state.accessToken
                    }
                }).then((response) => {
                    this.stocks = response.data
                }).catch((err) => {
                    console.log(err)
                })
                // if (result.data) {
                //     const data = await result.json()
                //     console.log(data)
                //     return response
                // }
                // else {
                //     console.log(result.data.message)
                // }
            } catch {
                console.log("Failed to get data");
            }
        },
        intervalFetchData: function () {
            setInterval(() => {
                this.getStockData();
            }, 5000);
        }
    },
    // async created() {
    //     this.stock = await this.getStockData()
    //     console.log(this.stock)
    // },
    mounted() {
        // Run once when mounted
        this.getStockData()
        // Run the intervalFetchData function once to set the interval time for later refresh
        this.intervalFetchData();
    }
}
</script>

<style scoped>
table, th, td {
    border: 1px solid;
    position: relative;
    overflow: auto;
    margin: 15px auto;
    padding: 5px;
}
</style>