---
tags:
- RequirementType
title: REQUIREMENT_PLOT_HAS_FALLOUT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_HAS_FALLOUT
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="PLOT_IN_FALLOUT"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"PLOT_IN_FALLOUT",
		"REQUIREMENT_PLOT_HAS_FALLOUT"
	);

```
