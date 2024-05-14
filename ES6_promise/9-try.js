export default function guardrail(mathFunction) {
  let mathFunc;
  const queue = [];

  try {
    mathFunc = mathFunction();
  } catch (error) {
    mathFunc = error.toString();
  }
  queue.push(mathFunc);
  queue.push('Guardrail was processed');

  return queue;
}
