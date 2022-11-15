<template>
    <h1>test</h1>
</template>

<script>
export default {
    name: 'DashboardView',
    data() {
        return {
            stock: [],
        }
    },
    methods: {
        async getStockData() {
            const res = await fetch('redis://redis:6379')

            const data = await res.json()

            return data
        }
    },
    async created() {
        this.stock = await this.getStockData()
        console.log(this.stock)
    }
}
</script>