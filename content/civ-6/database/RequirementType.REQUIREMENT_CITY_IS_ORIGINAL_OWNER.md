---
tags:
- RequirementType
title: REQUIREMENT_CITY_IS_ORIGINAL_OWNER
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_IS_ORIGINAL_OWNER
>
> * Class: `CITIES`
> * Arguments:
>	* **This RequirementType has no Arguments**

## Samples

```SQL {title="CITY_IS_NOT_ORIGINAL_OWNER_REQUIREMENTS"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"CITY_IS_NOT_ORIGINAL_OWNER_REQUIREMENTS",
		"REQUIREMENT_CITY_IS_ORIGINAL_OWNER",
		1
	);


```
