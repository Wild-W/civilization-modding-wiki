---
tags:
- RequirementType
title: REQUIREMENT_PLOT_HAS_ANY_IMPROVEMENT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_HAS_ANY_IMPROVEMENT
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLOT_HAS_NO_IMPROVEMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_NO_IMPROVEMENT",
		"REQUIREMENT_PLOT_HAS_ANY_IMPROVEMENT",
		1
	);

```
