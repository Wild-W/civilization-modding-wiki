---
tags:
- RequirementType
title: REQUIREMENT_PLOT_UNIT_FLANKED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_UNIT_FLANKED
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="UNIT_IS_FLANKED_REQUIREMENT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"UNIT_IS_FLANKED_REQUIREMENT",
		"REQUIREMENT_PLOT_UNIT_FLANKED"
	);

```
