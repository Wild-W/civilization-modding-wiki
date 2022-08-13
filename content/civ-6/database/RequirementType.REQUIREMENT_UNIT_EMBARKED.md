---
tags:
- RequirementType
title: REQUIREMENT_UNIT_EMBARKED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_UNIT_EMBARKED
>
> * Class: `UNITS`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="REQUIRES_UNIT_IS_EMBARKED"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_UNIT_IS_EMBARKED",
		"REQUIREMENT_UNIT_EMBARKED"
	);


```
