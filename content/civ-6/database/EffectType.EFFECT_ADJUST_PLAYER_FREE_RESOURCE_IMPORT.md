---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_FREE_RESOURCE_IMPORT
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_FREE_RESOURCE_IMPORT
>
> * Class: `PLAYERS`
> * Parameters:
>	* Amount `Integer`
>	* ResourceType `String`
>		* [Resources.ResourceType]

## Samples

```SQL {title="MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_BONUS"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType,
		SubjectRequirementSetId
	)
VALUES
	(
		"MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_BONUS",
		"MODIFIER_PLAYER_ADJUST_FREE_RESOURCE_IMPORT",
		"PLAYER_HAS_NO_ALUMINUM"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_BONUS",
		"Amount",
		1
	),
	(
		"MINOR_CIV_HATTUSA_ALUMINUM_RESOURCE_BONUS",
		"ResourceType",
		"RESOURCE_ALUMINUM"
	);
	
```

