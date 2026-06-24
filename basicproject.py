import pandas as pd
import matplotlib.pyplot as plt

# ── 1. Sample Student Data ──────────────────────────────────────────
data = {
    'Student': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve',
                'Frank', 'Grace', 'Henry', 'Iris', 'Jack'],
    'Math':    [85, 72, 90, 65, 88, 76, 95, 60, 82, 70],
    'Science': [78, 85, 88, 70, 92, 65, 80, 75, 90, 68],
    'English': [90, 68, 75, 80, 85, 72, 88, 65, 78, 82],
    'History': [70, 80, 65, 88, 75, 90, 72, 85, 68, 78],
}

df = pd.DataFrame(data)

# ── 2. Add Total and Average columns ───────────────────────────────
df['Total']   = df[['Math', 'Science', 'English', 'History']].sum(axis=1)
df['Average'] = df['Total'] / 4

# ── 3. Print Full Report ───────────────────────────────────────────
print("=" * 60)
print("        STUDENT SCORE ANALYSIS REPORT")
print("=" * 60)
print(df[['Student', 'Math', 'Science', 'English', 'History',
          'Total', 'Average']].to_string(index=False))

print("\n" + "=" * 60)
print("           SUBJECT-WISE STATISTICS")
print("=" * 60)
subjects = ['Math', 'Science', 'English', 'History']
for sub in subjects:
    print(f"{sub:10s} | Avg: {df[sub].mean():.1f} | "
          f"Max: {df[sub].max()} | Min: {df[sub].min()}")

print("\n" + "=" * 60)
print("           TOP & BOTTOM PERFORMERS")
print("=" * 60)
top    = df.loc[df['Average'].idxmax()]
bottom = df.loc[df['Average'].idxmin()]
print(f"🏆 Top Scorer   : {top['Student']}  (Avg: {top['Average']:.1f})")
print(f"📉 Needs Support: {bottom['Student']}  (Avg: {bottom['Average']:.1f})")

# ── 4. Grade Assignment ────────────────────────────────────────────
def get_grade(avg):
    if avg >= 90: return 'A+'
    elif avg >= 80: return 'A'
    elif avg >= 70: return 'B'
    elif avg >= 60: return 'C'
    else: return 'D'

df['Grade'] = df['Average'].apply(get_grade)
print("\n" + "=" * 60)
print("           GRADES")
print("=" * 60)
for _, row in df.iterrows():
    print(f"{row['Student']:10s} → Average: {row['Average']:.1f}  Grade: {row['Grade']}")

# ── 5. Charts ──────────────────────────────────────────────────────
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle('Student Score Analysis', fontsize=16, fontweight='bold')

# Chart 1: Average score per student
axes[0].bar(df['Student'], df['Average'], color='steelblue', edgecolor='black')
axes[0].set_title('Average Score per Student')
axes[0].set_xlabel('Student')
axes[0].set_ylabel('Average Score')
axes[0].tick_params(axis='x', rotation=45)
axes[0].axhline(df['Average'].mean(), color='red', linestyle='--', label='Class Avg')
axes[0].legend()

# Chart 2: Subject-wise average
subject_avgs = [df[s].mean() for s in subjects]
axes[1].bar(subjects, subject_avgs, color=['#FF6B6B','#4ECDC4','#45B7D1','#96CEB4'],
            edgecolor='black')
axes[1].set_title('Subject-wise Average Score')
axes[1].set_xlabel('Subject')
axes[1].set_ylabel('Average Score')
axes[1].set_ylim(0, 100)

# Chart 3: Grade distribution pie chart
grade_counts = df['Grade'].value_counts()
axes[2].pie(grade_counts.values, labels=grade_counts.index, autopct='%1.1f%%',
            colors=['#2ECC71','#3498DB','#F39C12','#E74C3C','#9B59B6'])
axes[2].set_title('Grade Distribution')

plt.tight_layout()
plt.savefig('student_analysis_chart.png', dpi=150, bbox_inches='tight')
plt.show()
print("\n✅ Chart saved as 'student_analysis_chart.png'")
print("✅ Analysis Complete!")