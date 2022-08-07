---
tags:
- EffectType
title: EFFECT_ADJUST_PLAYER_VALID_BUILDING
---
This is an [Effect Type](civ-6/database/articles/effect-types.md). Please refer to that page for more information on Effect Type

## Info
> [!info] EFFECT_ADJUST_PLAYER_VALID_BUILDING
>
> * Class: `Unknown`
> * Parameters:
>	* BuildingType `Unknown`
>	* BuildingTypeToReplace `Unknown`

## Samples
```SQL {title="GOVERNOR_PROMOTION_OWLS_OF_MINERVA_2_UNLOCK_GILDED_VAULT"}
INSERT INTO Modifiers
	(
		ModifierId,
		ModifierType
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_2_UNLOCK_GILDED_VAULT",
		"MODIFIER_PLAYER_ADJUST_VALID_BUILDING"
	);

INSERT INTO ModifierArguments
	(
		ModifierId,
		Name,
		Value
	)
VALUES
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_2_UNLOCK_GILDED_VAULT",
		"BuildingType",
		"BUILDING_GILDED_VAULT"
	),
	(
		"GOVERNOR_PROMOTION_OWLS_OF_MINERVA_2_UNLOCK_GILDED_VAULT",
		"BuildingTypeToReplace",
		"BUILDING_BANK"
	);
	
```

