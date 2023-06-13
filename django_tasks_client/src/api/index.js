import instance from './instance'

import testModule from './test'
import sessionModule from './session'
import questionModule from './question'
import answerModule from './answer'

export default {
  tests: testModule(instance),
  sessions: sessionModule(instance),
  questions: questionModule(instance),
  answers: answerModule(instance),
}
