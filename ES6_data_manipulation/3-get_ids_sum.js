export default function getStudentIdsSum(students) {
  if (!Array.isArray(students)) return [];
  return students.reduce((acc, student) => acc + student.id, 0);
}
