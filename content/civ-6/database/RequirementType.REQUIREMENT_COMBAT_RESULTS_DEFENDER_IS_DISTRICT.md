---
tags:
- RequirementType
title: REQUIREMENT_COMBAT_RESULTS_DEFENDER_IS_DISTRICT
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_COMBAT_RESULTS_DEFENDER_IS_DISTRICT
>
> * Class: `Unknown`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIREMENT_DISTRICT_DEFENDER"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIREMENT_DISTRICT_DEFENDER",
		"REQUIREMENT_COMBAT_RESULTS_DEFENDER_IS_DISTRICT"
	);


```
