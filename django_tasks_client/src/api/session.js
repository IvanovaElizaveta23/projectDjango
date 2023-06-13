export default function(instance) {
  return {
    getAll(id) {
      return instance.get(`user/${id}/session/`)
    }
  }
}