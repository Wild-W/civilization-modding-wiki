---
tags:
- RequirementType
title: REQUIREMENT_CITY_HAS_RESOURCE_TYPE_IMPROVED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_CITY_HAS_RESOURCE_TYPE_IMPROVED
>
> * Class: `CITIES`
> * Arguments:
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples

```SQL {title="REQUIRES_CITY_HAS_IMPROVED_ALUMINUM"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType
	)
VALUES
	(
		"REQUIRES_CITY_HAS_IMPROVED_ALUMINUM",
		"REQUIREMENT_CITY_HAS_RESOURCE_TYPE_IMPROVED"
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_CITY_HAS_IMPROVED_ALUMINUM",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	```
