---
tags:
- RequirementType
title: REQUIREMENT_PLOT_RESOURCE_VISIBLE
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLOT_RESOURCE_VISIBLE
>
> * Class: `PLOTS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_PLOT_HAS_VISIBLE_RESOURCE"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_PLOT_HAS_VISIBLE_RESOURCE",
		"REQUIREMENT_PLOT_RESOURCE_VISIBLE"
	);

```
