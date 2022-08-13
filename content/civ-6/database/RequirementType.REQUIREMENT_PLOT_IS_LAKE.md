---
tags:
- RequirementType
title: REQUIREMENT_PLOT_IS_LAKE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_IS_LAKE
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="PLOT_IS_NOT_LAKE_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"PLOT_IS_NOT_LAKE_REQUIREMENTS",
		"REQUIREMENT_PLOT_IS_LAKE",
		1
	);


```
