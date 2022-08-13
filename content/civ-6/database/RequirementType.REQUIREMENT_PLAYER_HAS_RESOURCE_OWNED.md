---
tags:
- RequirementType
title: REQUIREMENT_PLAYER_HAS_RESOURCE_OWNED
---
This is a [Requirement Type](civ-6/database/articles/requirement-types.md). Please refer to that page for more information on Requirement Types

## Info
> [!info] REQUIREMENT_PLAYER_HAS_RESOURCE_OWNED
>
> * Class: `PLAYERS`
> * Arguments:
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples

```SQL {title="REQUIRES_PLAYER_HAS_NO_ALUMINUM"}
INSERT INTO Requirements
	(
		RequirementId,
		RequirementType,
		Inverse
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_NO_ALUMINUM",
		"REQUIREMENT_PLAYER_HAS_RESOURCE_OWNED",
		1
	);

INSERT INTO RequirementArguments

	(
		RequirementId,
		Name,
		Value
	)
VALUES
	(
		"REQUIRES_PLAYER_HAS_NO_ALUMINUM",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	```
