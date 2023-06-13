export default function(instance) {
  return {
    get(id, page) {
      return instance.get(`test/${id}/question/${page}`)
    }
  }
}