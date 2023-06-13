export default function(instance) {
  return {
    get(id) {
      return instance.get(`test/${id}/`)
    },
    getAll() {
      return instance.get('test/')
    }
  }
}