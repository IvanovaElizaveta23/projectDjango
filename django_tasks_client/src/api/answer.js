export default function(instance) {
  return {
    getAll(id) {
      return instance.get(`question/${id}/answer/`)
    }
  }
}