---
tags:
- RequirementType
title: REQUIREMENT_PLOT_HAS_ANY_DISTRICT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_HAS_ANY_DISTRICT
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="DEFENDER_IS_OCCUPYING_DISTRICT_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"DEFENDER_IS_OCCUPYING_DISTRICT_REQUIREMENT",
		"REQUIREMENT_PLOT_HAS_ANY_DISTRICT"
	);


```
